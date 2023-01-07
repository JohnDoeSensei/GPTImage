from module.GPTImage import GPTImage
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="text to generate picture", type=str)
    parser.add_argument("-n", "--number", help="number of picture generated", type=int)
    parser.add_argument("-s", "--size", help="size of picture (256x256, 512x512, 1024x1024)", type=str)
    args = parser.parse_args()
    print('[+] Generating image from the text: '+str(args.prompt))
    gpt_img = GPTImage()
    if args.number is None and args.size is None:
        gpt_img.create_img(args.prompt)
    elif args.size is None:
        gpt_img.create_img(args.prompt, n_img=args.number)
    elif args.number is None:
        gpt_img.create_img(args.prompt, size=args.size)
    else: 
        gpt_img.create_img(args.prompt, n_img=args.number, size=args.size)
    print('[+] Complete: '+str(gpt_img._img_path))

main()