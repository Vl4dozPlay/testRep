import math
import random


def en(i, e, n):
    k = len(str(n));

    result = 1;

    for j in range(e):
            result = result * i;
            result = result % n;

    if(k>len(str(result))):
        l = k - len(str(result));
        result = l*'0' + str(result);
    return result;

def encryption():
    s = '';
    s2 = '';
    decode ={
        'A':'1',
        'B':'2',
        'C':'3',
        'D':'4',
        'E':'5',
        'F':'6',
        'G':'7',
        'H':'8',
        'I':'9',
        'J':'10',
        'K':'11',
        'L':'12',
        'M':'13',
        'N':'14',
        'O':'15',
        'P':'16',
        'Q':'17',
        'R':'18',
        'S':'19',
        'T':'20',
        'U':'21',
        'V': '22',
        'W': '23',
        'X':'24',
        'Y':'25',
        'Z': '26',
        'a':'27',
        'b':'28',
        'c':'29',
        'd':'30',
        'e':'31',
        'f':'32',
        'g':'33',
        'h':'34',
        'i':'35',
        'j':'36',
        'k':'37',
        'l': '38',
        'm':'39',
        'n':'40' ,
        'o':'41',
        'p':'42' ,
        'q': '43',
        'r':'44' ,
        's':'45' ,
        't':'46' ,
         'u':'47',
        'v':'48' ,
        'w':'49' ,
        'x':'50' ,
        'y':'51' ,
        'z':'52' ,
        ' ': '53',
        '.':'54',
        ',':'55' ,
        '!':'56' ,
        '?':'57' ,
    }
   # with open("ecript.txt", "r") as f:
   #     for line in f:
    #       s+=line;
    #f.close();
    print('Введите сообщение!');
    ss= input();
    i = 0

    f = open('openkey.txt', 'r');
    f.readline();
    n = int(f.readline());
    e = int(f.readline());
    f.close();

    for i in range(len(ss)):
        s2 += str(en(int(decode[ss[i]]), e, n));

    f = open("dcript.txt", "w");
    f.write(s2);
    f.close();

def de(i, d, n):
    current = i;
    result = 1;

    for j in range(d):
        result = result * current;
        result = result % n;
    return result;

def decryption():
    s2 = '';
    s3 = '';
    s = '';
    encode = {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
        '9': 'I',
        '10': 'J',
        '11': 'K',
        '12': 'L',
        '13': 'M',
        '14': 'N',
        '15': 'O',
        '16': 'P',
        '17': 'Q',
        '18': 'R',
        '19': 'S',
        '20': 'T',
        '21': 'U',
        '22': 'V',
        '23': 'W',
        '24': 'X',
        '25': 'Y',
        '26': 'Z',
        '27': 'a',
        '28': 'b',
        '29': 'c',
        '30': 'd',
        '31': 'e',
        '32': 'f',
        '33': 'g',
        '34': 'h',
        '35': 'i',
        '36': 'j',
        '37': 'k',
        '38': 'l',
        '39': 'm',
        '40': 'n',
        '41': 'o',
        '42': 'p',
        '43': 'q',
        '44': 'r',
        '45': 's',
        '46': 'y',
        '47': 'u',
        '48': 'v',
        '49': 'w',
        '50': 'x',
        '51': 'y',
        '52': 'z',
        '53': ' ',
        '54': '.',
        '55': ',',
        '56': '!',
        '57': '?',
    }

    f = open('closekey.txt', 'r');
    f.readline();
    n = int(f.readline());
    f.readline();
    d = int(f.readline());
    f.close();

    k = len(str(n));

    f = open("dcript.txt", "r");
    ss = f.readline();
    i=0;
    for i in range(k, len(ss)+1, k):
        s2 = str(de(int(ss[i-k:i]), d, n));
        s += encode[s2];
    print(s)



    f = open("ecript.txt", "w");
    f.write(s3);
    f.close();


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    k=1;
    while (1):
        k = k + t;
        if (k % e == 0):
            d = (k / e);
            return round(d);


def exp():
    print("Выбирите экспоненту: (1) 3, (2) 5, (3) 17, (4) 257, (5) 65537");
    f = int(input());
    if(f == 1): return 3;
    elif (f == 2): return 5;
    elif (f == 3): return 17;
    elif (f == 4):return 257;
    else: return 65537



def rabinMiller(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True


def isPrime(num):
    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
                 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num)


def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if isPrime(num):
            return num

if __name__ == '__main__':
    print("Введите действие (1) генерация ключей, (2) шифрование, (3) расшифрование");
    dei = int(input());
    if(dei == 1):
        print("Введите размерность чисел p и q (степень двойки)");
        s = int(input());

        print("Генерируем p и q...");
        p= generateLargePrime(s);
        q= generateLargePrime(s);

        print("Считаем n, t...");
        n = p*q;

        t = (p - 1) * (q - 1);

        e = exp();
        print("Считаем d...");
        d = findModInverse(e, t);

        print("Записываем ключи");
        f =open('openkey.txt', 'w');
        f.write('RSAPublicKey ::= SEQUENCE {\n'+str(n)+'\n'+str(e)+'\n'+'}');
        f.close();

        f = open('closekey.txt', 'w');
        f.write('RSAPrivateKey ::= SEQUENCE {\n'+str( n) + '\n'+ str(e)+ '\n'+  str(d) +  '\n' + str(p) +  '\n' +  str(q) + '\n' '}');
        f.close();
    if (dei == 2): encryption();

    if(dei == 3): decryption();