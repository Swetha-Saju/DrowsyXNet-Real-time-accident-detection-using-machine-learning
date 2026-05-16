from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render,HttpResponse,redirect

from .import models

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        age=request.POST.get('Age')
        gender=request.POST.get('Gender')
        phone_no=request.POST.get('phone_no')
        state=request.POST.get('state')
        image=request.FILES.get('image')
        email=request.POST.get('email')
        password=request.POST.get('password')
        licenceno=request.POST.get(' licenceno')
        
        if models.Register.objects.filter(email=email).exists():
            return HttpResponse("this email already exist")
        else:
            user=models.Register(name=name,age=age,gender=gender,phone_no=phone_no,state=state,image=image,email=email,password=password, licenceno= licenceno)
            user.save()
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')
         try:
            user=models.Register.objects.get(email=email,)
            email=user.email
            request.session['email'] = email
            if password==password:
                return redirect('home')
            else:
                return HttpResponse('invalid email or password')
         except models.Register.DoesNotExist:
             return HttpResponse('this user doesnt exist')
    return render(request,'Login.html')

def logout(request):
    if'email'in request.session:
        request.session.flush()
        return redirect('index')
    return redirect('index')


def profile(request):
    if'email' in request.session:
        email=request.session['email']
        try:
            client=models.Register.objects.get(email=email)
            return render(request,'profile.html',{'client':client})
        except models.Register.DoesNotExist:
            return HttpResponse("user not found")
    else:
        return HttpResponse("page not found")
    
    
def editprofile(request):
    if'email' in request.session:
        email=request.session['email']
        
        try:  
            client=models.Register.objects.get(email=email)
            
            if request.method=="POST":
                client.name=request.POST.get('Name')
                client.age=request.POST.get('Age')
                client.gender=request.POST.get('Gender')
                client.phone_no=request.POST.get('phone_no') or client.phone_no
                client.state=request.POST.get('state')
                client.image=request.FILES.get('image') or client.image
                client.email=request.POST.get('email')
                client.password=request.POST.get('password') or client.password
                client.licenceno=request.POST.get('licenceno') or client.licenceno
                client.save()
                
                return redirect('profile')
            else:
                return render(request,'editprofile.html',{'client':client})
            
        except models.Register.DoesNotExist:
            return HttpResponse('user not found')
    else:
        return HttpResponse('email not found')
            
            
    
    
def adminlogin(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        adminusername="ADMIN"
        adminpassword="admin"
        if adminusername==username:
            if adminpassword==password:
                return redirect('adminhome')
            else:
                return redirect('adminlogin')
        else:
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')
    

    
    
def adminhome(request):
    return render(request,'adminhome.html')    




def userlist(request):
    user=models.Register.objects.all()
    return render(request,'userlist.html',{'u':user})


def deleteuserlist(request,id):
    user=models.Register.objects.filter(id=id)
    user.delete()
    return redirect('userlist')
    

def add_vehicle(request):
    if request.method == 'POST':
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_type = request.POST.get('vehicle_type')
        capacity = request.POST.get('capacity')
        status = request.POST.get('status')
        vehicle_image = request.FILES.get('vehicle_image')

      
        vehicle = models.Vehicle(
            vehicle_number=vehicle_number,
            vehicle_name=vehicle_name,
            vehicle_type=vehicle_type,
            capacity=capacity,
            status=status,
            image=vehicle_image
        )
        vehicle.save()

        return HttpResponse("<script>alert('Vehicle Added successfully');window.location.href='/vehicles/';</script>")
    
    else:
        return render(request, 'add_vehicle.html') 
    
    
def add_driver(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        license_number = request.POST.get('license')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        status = request.POST.get('status')
        photo = request.FILES.get('photo')

       
        driver = models.Driver(
            name=name,
            license_number=license_number,
            phone=phone,
            email=email,
            address=address,
            experience=experience,
            status=status,
            photo=photo
        )
        driver.save()

        return HttpResponse("<script>alert('Driver Added Successfully!');window.location.href='/drivers/';</script>")
    
    else:
        return render(request, 'add_driver.html')

def driver_list(request):
    drivers = models.Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})


def delete_driver(request,id):
    driver =models.Driver.objects.get(id=id)
    driver.delete()
    return redirect('driver_list')

def vehicle_list(request):
    vehicles = models.Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


def delete_vehicle(request,id):
    vehicles =models.Vehicle.objects.get(id=id)
    vehicles.delete()
    return redirect('vehicle_list')


from django.shortcuts import render
from django.http import HttpResponse
import cv2
import os

def capture_image(request):
    try:
        #initialize camera 
        cam = cv2.VideoCapture(0)  # 0 = default camera

        ret, frame = cam.read()
        if ret:
            # save image tO MEDIA directory
            image_path = os.path.join(settings.MEDIA_ROOT, 'captured_image.jpg')
            cv2.imwrite(image_path, frame)
            cam.release()

            return HttpResponse("image captured and saved as captured_image.jpg in MEDIA folder.")
        else:
            cam.release()
            return HttpResponse("camera not found or cannot capture frame.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    

def upload_documents(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        upload_documents=request.FILES.get('uploaded_documents')

        user=models.Upload_documents(name=name,description=description,uploaded_documents=upload_documents)
        user.save()
        return redirect('documents_list')
    return render(request,'documents.html')


def documents_list(request):
    documents = models.Upload_documents.objects.all()
    return render(request, 'documents_list.html', {'documents': documents})


def documents_delete(request,id):
    documents = models.Upload_documents.objects.get(id=id)
    documents.delete()
    return redirect('documents_list')


def Notification_alert(request,id):
    Notification = models.Notifications.objects.all()
    return render(request, 'Notification.html', {'Notification': Notification})


def camera(request):
    return render(request, 'camera.html')



import cv2
import dlib
import numpy as np
from django.http import StreamingHttpResponse
import threading
import winsound  # For default beep on Windows

# Load face detector & predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    "C:\\Users\\Swetha Saju\\programs\\Downloads\\smartdriver_org_16_11_2025\\smartdriver_org\\smartdriver\\smartdriverapp\\shape_predictor_68_face_landmarks.dat"
)

# Landmark indices
LEFT_EYE = list(range(36, 42))
RIGHT_EYE = list(range(42, 48))
MOUTH = list(range(60, 68))

# Eye Aspect Ratio
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# Mouth Aspect Ratio
def mouth_aspect_ratio(mouth):
    A = np.linalg.norm(mouth[2] - mouth[6])
    B = np.linalg.norm(mouth[3] - mouth[5])
    C = np.linalg.norm(mouth[0] - mouth[4])
    return (A + B) / (2.0 * C)

# Play alarm asynchronously
def play_alarm():
    threading.Thread(target=winsound.Beep, args=(1000, 500), daemon=True).start()

# Video stream generator
def gen():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

            left_eye = landmarks[LEFT_EYE]
            right_eye = landmarks[RIGHT_EYE]
            mouth = landmarks[MOUTH]

            # Compute EAR & MAR
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0
            mar = mouth_aspect_ratio(mouth)

            # Draw eye & mouth contours
            cv2.polylines(frame, [left_eye], True, (0,255,0), 1)
            cv2.polylines(frame, [right_eye], True, (0,255,0), 1)
            cv2.polylines(frame, [mouth], True, (0,0,255), 1)

            # Labels
            cv2.putText(frame, f"EAR: {ear:.2f}", (face.left(), face.top()-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            cv2.putText(frame, f"MAR: {mar:.2f}", (face.left(), face.top()-40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            # Trigger alarms
            if ear < 0.15:
                cv2.putText(frame, "DROWSY!", (face.left(), face.bottom()+20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
                play_alarm()
            if mar > 0.6:
                cv2.putText(frame, "YAWN!", (face.left(), face.bottom()+50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
                play_alarm()

        # Encode frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Django view for video feed
def video_feed(request):
    return StreamingHttpResponse(gen(),
                content_type='multipart/x-mixed-replace; boundary=frame')
