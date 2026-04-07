import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
        title: const Text("Perfil"),
        actions: const [
          Icon(Icons.share),
          SizedBox(width: 10),
          Icon(Icons.settings)
        ],
      ),

      body: SingleChildScrollView(
        child: Column(
          children: [

            /// STACK (BANNER + FOTO)
            Stack(
              alignment: Alignment.center,
              clipBehavior: Clip.none,
              children: [

                Container(
                  height: 150,
                  color: Colors.blue,
                ),

                const Positioned(
                  bottom: -50,
                  child: CircleAvatar(
                    radius: 50,
                    backgroundImage: NetworkImage(
                      "https://i.pravatar.cc/300",
                    ),
                  ),
                )
              ],
            ),

            const SizedBox(height: 60),

            const Text(
              "Carolline Maia Soares",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 10),

            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 20),
              child: Text(
                "Desenvolvedora com experiência em Java e Python, focada em aplicações web.",
                textAlign: TextAlign.center,
              ),
            ),

            const SizedBox(height: 20),

            /// REDES SOCIAIS
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                Icon(Icons.link),
                SizedBox(width: 15),
                Icon(Icons.code),
                SizedBox(width: 15),
                Icon(Icons.work),
              ],
            ),

            const SizedBox(height: 20),

            /// BADGES
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                badge("Projetos", "12"),
                badge("Seguidores", "540"),
                badge("Repos", "30"),
              ],
            ),

            const SizedBox(height: 20),

            atributo("Telefone", "1999326-9988"),
            atributo("Email", "carollinemaias@gmail.com"),
            atributo("Empresa", "Tech Solutions"),
            atributo("Localização", "Brasil"),
            atributo("Especialidade", "Flutter Developer"),

            const SizedBox(height: 20)
          ],
        ),
      ),

      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: "Perfil",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.work),
            label: "Projetos",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.contact_mail),
            label: "Contato",
          ),
        ],
      ),
    );
  }

  Widget badge(String titulo, String valor) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.blue.shade100,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        children: [
          Text(valor,
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 18,
              )),
          Text(titulo)
        ],
      ),
    );
  }

  Widget atributo(String titulo, String valor) {
    return ListTile(
      leading: const Icon(Icons.arrow_right),
      title: Text(titulo),
      subtitle: Text(valor),
    );
  }
}