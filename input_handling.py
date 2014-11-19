def handle_input():
    try:
        while True:
            print "Number please:",
            val = raw_input()
            
            try:
                number = int(val)
            except (ValueError):
                "ignore"
                pass
            else:
                return str(number)
            
    except (KeyboardInterrupt):
        return None
    
val = handle_input()
print "You entered:", val, "Thank you :)"