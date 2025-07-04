# We have to install 2 libraries 1.qrcode 2.pillow 
 
#STEP 1 : we will take users upi id as input. 
#STEP 2 :  we will mention upi id url and some more information. 
#STEP 3: we will generate qr id for payment app using function qr.make 
#STEP 4 : (optional) in this step we can save the generated qr as image in our system. 
#STEP 5 :  we will use pillow viewer to display the generated qr code

import qrcode

# Step 1: Get UPI ID input
upi_id = input("Enter your UPI ID: ")

# Step 2: Define URLs
#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE 
# above is the format of payment URL . pa ,apn parameters 
#pa = upi id in which we have to do the payment.
#pn = recipent name
#an = amount 
# c = currency (INR ) 
# tn = payment message 

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

print("✅ Payment URLs created.")

# Step 3: Generate QR codes

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

print("✅ QR codes generated.")

# Step 4: Save QR codes (OPTIONAL )

phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

print("✅ QR codes saved as PNG files.")

# Step 5: Show QR codes (this opens default image viewer)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

print("✅ QR codes displayed. Please check your image viewer.")

# Step 6: Pause to keep the terminal open
input("Press Enter to exit...")


