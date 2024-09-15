st = 'Print every word in this sentence that has an even number of letters'
split = st.split()
for a in split:
    if len(a)%2==0:
        print(a)
