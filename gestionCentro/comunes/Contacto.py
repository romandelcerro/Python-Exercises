class Contacto():
    def __init__(self,tlfs, email):
        self.tlfs = tlfs
        self.email = email

    def __str__(self):
        self.tlf_str = ', '.join(str(t) for t in self.tlfs)
        return f"{self.tlf_str} | {self.email}"

    def añadirTlf(self,tlf):
        self.tlfs.append(tlf)

    def eliminarTlf(self, tlf):
        if tlf in self.tlfs:
            self.tlfs.remove(tlf)
        else:
            print("No existe ese teléfono en la lista")