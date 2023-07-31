while True:
    try:
        name = input()
        nn = ''
        for ap in name:
            if ap == 'e':
                nn += 'i'
            elif ap == 'i':
                nn += 'e'    
            elif ap == 'E':
                nn += 'I' 
            elif ap == 'I':
                nn += 'E'
            else:
                nn += ap
    except:
        break
    
    
    print(nn)