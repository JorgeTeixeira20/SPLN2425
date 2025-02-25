# source venv/bin/activate

from jjcli import * 
'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    - s  fix me keep spaces 
    - e remove empty lines 
    - p print # when empty line is removed

'''

def remove_linhas_repetidas(cl): 
    linhas_vistas = set()
   
    for linha in cl.input(): 
        if "-e" not in cl.opt: 
            ln = linha.strip()
        else: 
            ln = linha 
        if not ln or ln not in linhas_vistas: 
            print(ln, end="\n")
            linhas_vistas.add(ln)
        if not ln:  
            if "-p" in cl.opt:
                print("#")  
            continue


def main (): 
    cl = clfilter(opt="s,e,p", man=__doc__)
    remove_linhas_repetidas(cl)

if __name__ == '__main__': 
    main()
