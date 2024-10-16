from  af09.aut import Token
from af09.help import Output, Ff,Jeda
 
import json,time,sys
from af09.send_request import Api


output = Output()  
api = Api()
ll = Ff().ll
jeda =Jeda()
output.banner()


def read_wallet_token(file_path='wallet_token.txt'):
        wallet_token_pairs = []

        # Membaca file wallet_token.txt
        with open(file_path, 'r') as f:
            # Membaca semua baris dari file
            lines = f.readlines()
            
            # Memproses setiap baris
            for line in lines:
                line = line.strip()  # Menghapus spasi atau newline
                if line:
                    # Memisahkan baris menjadi wallet dan token berdasarkan spasi
                    parts = line.split(' ')
                    if len(parts) == 2:
                        wallet = parts[0]
                        token = parts[1]
                        # Menambahkan pasangan wallet dan token ke dalam list
                        wallet_token_pairs.append((wallet, token))

        return wallet_token_pairs

def get_task(d):
    res=api.get(
        url='https://api-walletapp.waveonsui.com/api/mission/list',
        data={},
        token=d[1]
    )
    
    return res.json()

def claim_task(d,code_task):
    res=api.post(
        url   = 'https://api-walletapp.waveonsui.com/api/mission/submit',
        data  = {"code":code_task},
        token = d[1]
    )
    return res

def claim_earn(d):
    res=api.post(
        url   = 'https://api-walletapp.waveonsui.com/api/claim',
        data  = { "address":  d[0]},
        token = d[1]
    )
    return res
        

def main(wt):
    
    ### GET TASK
    tasks=get_task(wt)
    for task in tasks:
        
        claim=claim_task(wt,task['code'])
        if claim.status_code == 400 :
            claim= claim.json()
            output.danger(f"{task['name']} - {claim['message']}")
        elif claim.status_code == 200:
            output.success(f"{task['name']} - {claim['result']}")
            
    ### GET CLAIM EARNING
    res_claim_earn=claim_earn(wt)
    if(res_claim_earn.status_code==400):
        res_claim_js= res_claim_earn.json()
        output.danger(f"EARN - {res_claim_js['message']}")
    elif (res_claim_earn.status_code==200):
        res_claim_js= res_claim_earn.json()
        output.success(f"EARN - Claimed")
    else:
        res_claim_js= res_claim_earn.json()
        ll(res_claim_earn)
        
if __name__ == "__main__":
    while True:
        try:
            ### GET TOKEN
            wt=read_wallet_token()
            
            for i,d in enumerate(wt):
                main(d)
                time.sleep(10)
        except KeyboardInterrupt:
            print("Program dihentikan oleh pengguna (Ctrl+C)")
            break
        except Exception as e:
            print(f"Error tidak tertangani: {e}")
            continue
        jeda.countdown(1000)
