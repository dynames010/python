import argparse
parser = argparse.ArgumentParser(description='this is test_argparse')
parser.add_argument('-n1','--thisisn1',required=True,help='enter name')
parser.add_argument('--age',type=int,default=0,help='nice')


args = parser.parse_args()
print('-----------n1----------{}'.format(args.thisisn1))
print('--------------age---------{}'.format(args.age))