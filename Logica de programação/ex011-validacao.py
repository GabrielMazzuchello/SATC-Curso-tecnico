while True:
    name = str(input('Informe o seu nome: '))
    if len(name) < 3:
        age = int(input('Informe sua idade: '))
        if 0 < age < 100:
            sex = str(input('Informe seu sexo F paar feminino e M paar masculino: ')).upper()
            if (sex == 'F' or sex == 'M'):
                maritalstatus = str(input('Informe seu estado civil "S"-solteiro, "C"-Casado, "V"-Viuvo(a), "D"-Divorciado(a): ')).upper()
                if (sex == 'F' or sex == 'M') and (maritalstatus == 'S' or maritalstatus == 'C' or maritalstatus == 'V' or maritalstatus == 'D'):
                    wage = float(input('Informe seu salario: '))
                    if wage > 0:
                        print('Cadastro realizado com sucesso!')
                        break
                    else:
                        print('Salario Invalido!')
                else:
                    print('O estado civil informado é ivalodo!') 
            else:
                print('O sexo infomado é invalido!')     
        else:
            print('Idade incorreta Informe-a novamente!')
    else:
        print('Nome incorreto Informe-o novamente!')
        
