for i in range(2,21):
    with open(f'3tables/multiplication_table_of_{i}.txt','w') as f:
        for j in range(1,11):
            f.write(f'{i}X{j}={i*j}\n')
    break
