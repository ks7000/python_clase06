# -*- encoding=utf-8 -*-
import os
import sys
import glob
import click

@click.command()
@click.option('--archivo_original', prompt='"Introduzca el(los) nombre(s) de el(os) archivo(s) original(es):"', help='Se necesita un archivo origen al cual copiar y mostrar por pantalla.')
def lee(*args):
    for i in args:
        if isinstance(i,str):
            #if os.access(i, os.R_OK): 
            if existe_archivo(i):
                arch = raw_input("Introduzca el nombre del archivo a copiar:");
                if arch<> "":
                    copiar = False                    
                    if os.path.exists(arch):
                        resp = raw_input("El archivo existe, ¿Desea sobreescribirlo? [s/n]");
                        if resp == "s" or resp == "S":
                            copiar = True
                    else:
                        copiar = True
                    if copiar:                    
                        f = open(i)
                        g = open(arch, "w")
                        g.write("Este archivo fue copiado de ")
                        g.write(os.path.realpath(i))
                        for linea in f:
                            print linea
                            g.write(linea)
                        f.close()
                        g.close()
                        lee_archivo_varias_lineas(i)
            else:
                print "El archivo no existe."

def existe_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        resp = raw_input("El archivo NO existe, ¿Desea crearlo? [s/n]");
        if resp == "s" or resp == "S":
            if sys.platform == "linux2":
                os.system('touch ' + archivo )
            return True
        else:
            return False

def lee_archivo_varias_lineas(archivo):
    f=open(archivo)
    print "--------------------------------"
    print "Lee varias lineas sin ciclo for:"
    print (f.readlines())
    f.close
     
if __name__ == '__main__':
    if sys.platform == "linux2":
        os.system('clear')
    print glob.glob('*.txt')
    lee()
