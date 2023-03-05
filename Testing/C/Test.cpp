// 

#include <gtkmm.h>
#include <iostream>

class HelloWorld : public Gtk::Window
{
public:
  HelloWorld()
  {
    m_button.set_label("Click me!");
    m_button.signal_clicked().connect(sigc::mem_fun(*this,
              &HelloWorld::on_button_clicked));

    add(m_button);
    show_all_children();
  }

protected:
  void on_button_clicked()
  {
    std::cout << "Hello, world!" << std::endl;
  }

  Gtk::Button m_button;
};

int main(int argc, char* argv[])
{
  auto app = Gtk::Application::create(argc, argv, "org.gtkmm.examples.base");

  HelloWorld helloworld;

  return app->run(helloworld);
}
