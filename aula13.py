class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("Preço inválido")

produto = Produto("Notebook", 3000)
produto.set_preco(-3500)
produto.set_preco(3500)
print(produto.get_preco())


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def __str__(self):
        return f"Playlist: {self.nome}"

    def __len__(self):
        return len(self.musicas)
    
    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)
    
playlist = Playlist("Favoritas")
playlist.adicionar_musica("ballon in love")
playlist.adicionar_musica("cant stop the feeling")
print(playlist)
print(len(playlist))
playlist.listar_musicas()