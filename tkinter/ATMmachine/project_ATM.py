#consider current balance amount is 20000
Balance = 20000
print("\nWelcome To Z_U_D_K ATM--------Z_U_D_K बँक मध्ये आपले स्वागत आहे ")
print("Insert Your Card first!-------प्रथम तुमचे ATM कार्ड टाका")
print("Select language for further procedure")
print("1.English--press 1"
      "\n2.मराठी--२ दाबा "
      "\n3.हिन्दी--३ दबाए ")
lang = int(input())
if(lang==1):
      print("Enter Your 4 digit PIN number")
      m= int(input())
      print("1.Transfer Funds\t\t2.Fast Cash"
            "\n3.Balance Enquiry\t\t4.Withdrawl"
            "\n5.Mini Statment\t\t\t6.Cash Deposit"
            "\n7.Mobile Recharge\t\t8.PIN Change")
      x=int(input())
      if(x==4):
            print("Enter Amount\t")
            w=int(input())
            print("processing....")
            print("Collect Cash")
            R_B = Balance - w
            print("Remaining Balance\t",R_B)
      elif(x==8):
            print("Enter Your Old PIN number\t")
            n=int(input())
            if(n==m):
                  print("Enter the OTP received on Your Registered Mobile Number\t")
                  int(input())
                  print("Enter New PIN\t")
                  p=int(input())
                  print("Confirm New PIN\t")
                  q =int(input())
                  if(q==p):
                        print("PIN Changed Successfully!")
                  else:
                        print("Error!")
            else:
                  print("PIN Doesn't Match!")
      elif(x==3):
            print("Processing...")
            print("Your current Balance is",Balance)
            print("Take the Slip")
      elif(x==1):
            print("Processing...")
      elif (x == 2):
            print("Processing...")
      elif (x == 5):
            print("Processing...")
      elif (x == 6):
            print("Deposit per Transition Limit:\n200000")
            print("Service Charge:\n0")
            print("Acceptable Domination:\tRs.100 , Rs.200 , Rs.500 , Rs.2000")
            print("Please insert Your Cash")
            print("Press Enter to proceed")
            print("")
      elif (x == 7):
            print("Processing...")

      else:
            print("Error!")
elif(lang==2):
      print("तुमचा पिन नंबर टाका ")
      m = int(input())
      print("1.निधी हस्तांतरित \t\t2.जलद रोख "
            "\n3.बाकी रक्कम चौकशी\t4.पैसे काढणे "
            "\n5.छोटे विधान \t\t\t6.रोख ठेव "
            "\n7.मोबईल रीचार्ज \t\t8.PIN बदला ")
      x = int(input())
      if (x == 4):
            print("रक्कम प्रविष्ट करा \t")
            w = int(input())
            print("प्रक्रिया करीत आहे ....")
            print("रोख गोळा करा ")
            R_B = Balance - w
            print("बाकी रक्कम \t", R_B)
      elif (x == 8):
            print("तुमचा मागील पिन नंबर प्रविष्ट करा \t")
            n = int(input())
            if (n == m):
                  print("तुमच्या नोंदणीकृत मोबाइल क्रमांकावर प्राप्त झालेला OTP प्रविष्ट करा \t")
                  int(input())
                  print("नवीन पिन प्रविष्ट करा \t")
                  p = int(input())
                  print("नवीन पिन नक्की करा \t")
                  q = int(input())
                  if (q == p):
                        print("PIN यशस्वीरीत्या परिवर्तीत झाला !")
                  else:
                        print("त्रुटि!")
            else:
                  print("PIN जुळत नाही!")
      elif (x == 3):
            print("प्रक्रिया करीत आहे...")
            print("शिल्लक रक्कम\t", Balance)
            print("स्लिप घ्या !")
      elif (x == 1):
            print("प्रक्रिया करीत आहे...")
      elif (x == 2):
            print("प्रक्रिया करीत आहे...")
      elif (x == 5):
            print("प्रक्रिया करीत आहे...")
      elif (x == 6):
            print("प्रक्रिया करीत आहे...")
      elif (x == 7):
            print("प्रक्रिया करीत आहे...")

      else:
            print("त्रुटि!")
elif(lang==3):
      print("अपना पिन नंबर दर्ज करें")
      m = int(input())
      print("1.धनराशी का ट्रान्सफर\t2.तेज नगद  "
            "\n3.शेष रक्कम पुछ \t4.नकद निकासी"
            "\n5.मिनी स्टंटमेंट\t\t\t6.नकद जमा  "
            "\n7.मोबईल रीचार्ज \t\t8.PIN परिवर्तन")
      x = int(input())
      if (x == 4):
            print("राशी डाले \t")
            w = int(input())
            print("प्रक्रिया हो रही है....")
            print("नकद जमा करे")
            R_B = Balance - w
            print("शेष राशी\t", R_B)
      elif (x == 8):
            print("अपना पिछला पिन नंबर दर्ज करें \t")
            n = int(input())
            if (n == m):
                  print("अपने पंजीकृत मोबाइल नंबर पर प्राप्त OTP दर्ज करे\t")
                  int(input())
                  print("नया पिन दर्ज करे \t")
                  p = int(input())
                  print("अपने नये पिन की पुष्टी करे\t")
                  q = int(input())
                  if (q == p):
                        print("OTP सफलता पूर्वक बदला गया !")
                  else:
                        print("गलती!")
            else:
                  print("PIN मेल नही खाता!")
      elif (x == 3):
            print("प्रक्रिया हो रही है...")
            print("शेष राशी\t", Balance)
            print("स्लिप लीजीये!")
      elif (x == 1):
            print("प्रक्रिया हो रही है...")
      elif (x == 2):
            print("प्रक्रिया हो रही है...")
      elif (x == 5):
            print("प्रक्रिया हो रही है...")
      elif (x == 6):
            print("प्रक्रिया हो रही है...")
      elif (x == 7):
            print("प्रक्रिया हो रही है...")

      else:
            print("गलती!")
else:
      print("select proper language!\tयोग्य भाषा निवडा!\tउचित भाषा का चयन करे!")


