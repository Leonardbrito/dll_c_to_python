# dll_c_to_python
1.Crie um novo arquivo e escreva, por exemplo, uma função que some dois números e retorne o resultado.
  Chegar exemplo presente no repositorio
2.Se você estiver usando Windows, __declspec(dllexport) é necessário para adicionar a diretiva de exportação ao arquivo objeto e tornar a função acessível sem usar um arquivo .def. Se você estiver usando Linux, ele poderá ser omitido.
3. você pode usar gcc/g++ para compilar o programa e criar o .dll
4. gcc -shared -o nomedoarquivoc.dll nomedoarquivoc.c
5.chame seu dll em um arquivo python 
  veja o exemplo do arquivo python presente nesse repositorio
