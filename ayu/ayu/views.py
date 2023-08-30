from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

from ayuapp.models import Contact


# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='admin123',
    database='ayuchat'
)

# Retrieve the data from the chat table
my_cursor = conn.cursor()
my_cursor.execute("SELECT * FROM chat")
data = my_cursor.fetchall()

# Close the database connection
my_cursor.close()
conn.close()

# Create a new chatbot instance
chatbot = ChatBot('Ayu')

# Create a new trainer and train the chatbot using the retrieved data
trainer = ListTrainer(chatbot)
for conversation in data:
    trainer.train([conversation[1], conversation[2]])

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            message = data['message']
            
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='admin123',
                database='ayuchat'
            )
            
            # Search for each word in the database
            words = message.split()
            results = []

            for word in words:
                if len(word) > 4:
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT * FROM chat WHERE symptoms LIKE %s", ("%" + word + "%",))
                    data = my_cursor.fetchall()
                    my_cursor.close()
        
                    if data and len(data) > 0:
                        # Add the remedy to the results list
                        results.extend([row[2] for row in data])

            
            # Close the database connection
            conn.close()
            
            # Prepare the response data
            if results:
                response_text = " ".join(set(results))
            else:
                response_text = chatbot.get_response(message).text
            
            response_data = {
                'status': 'ok',
                'response': response_text
            }
            return JsonResponse(response_data)
        
        except Exception as e:
            error_data = {
                'status': 'error',
                'error_message': str(e)
            }
            return JsonResponse(error_data)
        
    else:
        error_data = {
            'status': 'error',
            'error_message': 'Only POST requests are allowed'
        }
        return JsonResponse(error_data)
def chat(request):
    return render(request, 'chat.html')
def home(request):
    return render(request, 'home.html')
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def admin(request):
    return render(request, 'admin.html')