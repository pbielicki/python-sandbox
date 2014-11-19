import cx_Oracle, random, time, datetime

guest = ['SANCHEZ' , 'MARTINEZ', 'LOMBARD', 'BIELICKI', 'NGUYEN', 'PERON'
         , 'MARIA', 'ARNEDO', 'LEXTRAIT', 'MOURGUES', 'KOWALSKI', 'SMITH'
         , 'DUMNAY', 'LAUNAY', 'LAGRAND', 'HORNET', 'BUFFON', 'WENGER', 'ARTUS'
         , 'GUMINSKI', 'WENT', 'GALDWIN', 'BAMBROUGH', 'ALMERAS', 'PRON', 'FLICK'
         , 'GABRIEL', 'HAMON', 'PELLERIN', 'PENNEL', 'PONT', 'LAROSA', 'JOSEPH'
         , 'MORARD', 'POUCET', 'AMBURATORE', 'VINCI', 'KLUCHA', 'GARBRYSIK', 'SCHYMALLA'
         , 'MOTTE', 'PASCAL', 'EMILE', 'STASINOS', 'VIET', 'PLOT', 'GENTIL'
         , 'KESES', 'BRUNET', 'NAJJAR', 'LEVY', 'HUARD', 'FOTSO', 'MARTIN'
         , 'BILLON', 'RONALDO']

agent = ['Maria', 'Anna', 'Mark', 'John', 'Alice', 'Bob', 'Nuno', 'Jeff', 'Susan', 'Bill', 'Joanna']
reason = ['new folio', 'check in', 'walk in', 'n/a', 'standard', 'check-in', 'new guest']
rate = ['BAR', 'FOO', 'GOV', 'MIL', 'PRO', 'COM', 'COR']

con = cx_Oracle.connect('godben11/amadeus@ncegcolnx123:15011/BEN11')
random = random.Random()

start = time.time()
size = 60000

for i in xrange(size + 1):
    cursor = con.cursor()
    checkin = datetime.date.today() + datetime.timedelta(days=random.randint(1, 10))
    checkout = checkin + datetime.timedelta(days=random.randint(1, 10))
    
    cursor.execute("INSERT INTO Folio_PRD(oid, property_id, agent_name, reason, room_id,"
                   + "rate_plan, guest_name, reservation_number, reservation_status, " 
                   + "checkin_date, checkout_date, creation_date, last_modification)" 
                   + "VALUES (folio_prd_pk.nextval, :pid, :agent, :reason, :room,"
                   + ":ratePlan, :guest, :resNumber, :resStatus, :checkin, :checkout, "
                   + "sysdate, sysdate)",
                   {
                    'pid' : "FR456890",
                    'agent' : agent[i % len(agent)],
                    'reason' : reason[i % len(reason)],
                    'room' : random.randint(1, 1000),
                    'ratePlan' : reason[i % len(rate)],
                    'guest' : guest[i % len(guest)],
                    'resNumber' : random.randint(50000, 1000000),
                    'resStatus' : random.randint(1, 4),
                    'checkin' : checkin,
                    'checkout' : checkout
                   }
                  )
    
    if i % 10000 == 0:
        cursor.close()
        con.commit()
        print str(i) + " folios added (" + str((i / float(size)) * 100.0) + "%)"
        print time.strftime("%H:%M:%S elapsed", time.gmtime(time.time() - start))
        
cursor.close()
con.commit()
print time.strftime("Total %H:%M:%S elapsed", time.gmtime(time.time() - start))