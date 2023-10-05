package cal;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calculator extends Frame implements ActionListener {

	// Labels
	Label lbl1, lbl2, lbl3;
	//
	TextField txt1, txt2, txt3;
	// Buttons
	Button btn1, btn2, btn3, btn4, btn5 ,btn6;

	public Calculator() {
		lbl1 = new Label("num1");
		lbl2 = new Label("num2");
		lbl3 = new Label("result");

		txt1 = new TextField(10);
		txt2 = new TextField(10);
		txt3 = new TextField(10);

		btn1 = new Button("Add");
		btn2 = new Button("Sub");
		btn3 = new Button("Multiply");
		btn4 = new Button("Divide");
		btn5 = new Button("Power");
		btn6 = new Button("Reset");

		add(lbl1);
		add(txt1);

		add(lbl2);
		add(txt2);

		add(lbl3);
		add(txt3);

		add(btn1);
		add(btn2);
		add(btn3);
		add(btn4);
		add(btn5);
		add(btn6);

		setSize(200, 200);
		setTitle("My Calculator");

		setLayout(new FlowLayout());

		btn1.addActionListener(this);
		btn2.addActionListener(this);
		btn3.addActionListener(this);
		btn4.addActionListener(this);
		btn5.addActionListener(this);
		btn6.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		float a = 0f, b = 0f, c = 0f;

		a = Float.parseFloat(txt1.getText());
		b = Float.parseFloat(txt2.getText());

	
		if (e.getSource() == btn1) {
			c = a + b;

		} else if (e.getSource() == btn2) {
			c = a - b;
		} else if (e.getSource() == btn3) {
			c = a * b;
		} else if (e.getSource() == btn4) {
			c = a / b;
		}
		else if (e.getSource() == btn5) {
			c =(float) Math.pow(a, b);
		}
		else if (e.getSource() == btn6) {
			txt1.setText("");
			txt2.setText("");
			txt3.setText("");
		}
		
		
		if(e.getSource()!=btn6)
		txt3.setText(c + "");

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calculator calc = new Calculator();
		calc.setVisible(true);// Windows must be visible
		calc.setLocation(300, 300);// from top right corner

	}

}
