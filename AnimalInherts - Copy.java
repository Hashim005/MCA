class Animal{
	void eat()
	{
		System.out.println("eating");
	}
}
	class Dog extends Animal
	{
		void barg()
		{
			System.out.println("barg...");
		}
	}
	class cat extends Animal{
		void  myaw(){
			System.out.println("myaw...myaw...");
		}
	}
	class AnimalInherts(){
		public static void main(String[] args){
		Dog d = new Dog();
		cat c = new cat();
		d.eat();
		d.barg();
		c.myaw();
	}
	}
