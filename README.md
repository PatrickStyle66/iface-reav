# iface-reav
Sistema criado para a reavaliação da disciplina *Projeto de Software*.

# Padrões de Projeto
-Implementado o padrão **Memento** na classe `UserClass` para a funcionalidade *Undo* na edição de perfil de usuário, utilizando classes aninhadas e o auxílio da classe `caretaker`

-Implementado o padrão **Observer** na classe `group` para a funcionalidade de postagens, posts só serão enviados aos usuários que fizerem parte do grupo. O Padrão foi implementado sem uma interface tendo em vista que só existe apenas um tipo de *Publisher* (os grupos)
