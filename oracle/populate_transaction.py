import cx_Oracle, random, time

pid = ['FR123456', 'DE23456', 'FRNCE12', 'PL23847', 'DE37377', 'FR45678', 'ES49888', 'FRPAR123', 'DE33345']
label = ['drink'
         , 'room bar'
         , 'external expense'
         , 'exceptional service'
         , 'restaurant'
         , 'spa + massage'
         , 'laundry'
         , 'flowers (exceptional)'
         , 'champagne'
         , 'party (concierge)'
         , 'special taxi'
         , 'translation'
         , 'exceptional room cleaning'
         , 'damages'
         , 'room upgrade'
         , 'hirdresser'
         , 'beauty parlor'
         , 'airport transfer'
         , 'extra taxi']

cur = ['EUR', 'PLN', 'GPB', 'SEK', 'NEK', 'DEK', 'CHF', 'USD', 'THB', 'HUF']
agent = ['Maria', 'Anna', 'Mark', 'John', 'Alice', 'Bob', 'Nuno', 'Jeff', 'Susan', 'Bill', 'Joanna']

con = cx_Oracle.connect('godben11/amadeus@ncegcolnx123:15011/BEN11')
random = random.Random()

start = time.time()
range = 30000000

for i in xrange(range + 1):
    cursor = con.cursor()
    price = random.random() * 100.0
    tax = random.random() * price
    
    cursor.execute("INSERT INTO Transaction_PRD(oid, property_id, tr_code, tr_type, tr_special_type, "
                   + "tr_label, quantity, unit_price, taxes, currency, agent_name, folio_id, "
                   + "creation_date, last_modification)" 
                   + "VALUES (transaction_prd_pk.nextval, :pid, :code, :type, :stype,"
                   + ":label, :quantity, :price, :taxes, :currency, :agent, :folio, "
                   + "sysdate, sysdate)",
                   {
                    'pid' : pid[i % len(pid)],
                    'code' : random.randint(1, 20),
                    'type' : random.randint(1, 30),
                    'stype' : random.randint(1, 25),
                    'label' : label[i % len(label)],
                    'quantity' : random.randint(1, 10),
                    'price' : price,
                    'taxes' : tax,
                    'currency' : cur[random.randint(0, len(cur) - 1)],
                    'agent' : agent[i % len(agent)],
                    'folio' : random.randint(1, 100000)
                   }
                  )
    
    if i % 10000 == 0:
        cursor.close()
        con.commit()
        print str(i) + " transactions added (" + str((i / float(range)) * 100.0) + "%)"
        print time.strftime("%H:%M:%S elapsed", time.gmtime(time.time() - start))