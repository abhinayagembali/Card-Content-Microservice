import requests
import base64

#put he images here to test...
l = [r'C:\Users\ABHINAYA GEMBALI\OneDrive\Desktop\TURTILPROJECT\output_images\stu_001.png',
     r'C:\Users\ABHINAYA GEMBALI\OneDrive\Desktop\TURTILPROJECT\output_images\stu_002.png',
     r'C:\Users\ABHINAYA GEMBALI\OneDrive\Desktop\TURTILPROJECT\output_images\stu_003.png',
     r'C:\Users\ABHINAYA GEMBALI\OneDrive\Desktop\TURTILPROJECT\output_images\stu_004.png',
     r'C:\Users\ABHINAYA GEMBALI\OneDrive\Desktop\TURTILPROJECT\output_images\abhi.png']


for i in l:
    # Read an image file
    with open(i, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode()

        # Send to API
        response = requests.post('http://localhost:8000/extract', 
                                json={'image': image_data, 'threshold': 0.7})

        # Print results
        print("\n\nOutput for image: ",i,"\n")
        print(response.json())