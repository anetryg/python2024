""" 
Vaším úkolem bude vytvořit program, který bude uchovávat informace o počítačích v síti.
Vytvořte třídu Network, která bude obsahovat tyto vlastnosti:
   computers (list[Computer]) - seznam počítačů v síti
Vytvořte třídu Computer, která bude obsahovat tyto vlastnosti a metody:
   name (str) - jméno počítače
   ip_address (str) - IP adresa počítače
   status (str) - stav počítače (online nebo offline)
   connect(self): připojí počítač k síti (nastaví self.status na "online")
   disconnect(self): odpojí počítač od sítě (nastaví self.status na "offline")
   `__str__`: vrátí textovou reprezentaci objektu
Vytvořte třídu `Server`, která dědí od třídy `Computer` a bude obsahovat navíc:
   `is_backup` (bool) - indikuje, zda je server záložní
   `__str__`: vrátí textovou reprezentaci objektu
Vytvořte třídu User, která bude obsahovat tyto vlastnosti:
   username (str) - uživatelské jméno
   connected_computers (list[Computer]) - seznam počítačů, ke kterým je uživatel připojen
   `__str__`: vrátí textovou reprezentaci objektu

Nakonec vytvořte ukázkový příklad, kde vytvoříte síť, několik počítačů a uživatelů, kteří se připojí k počítačům, přičemž náhodně určíte stav online/offline.
"""