package main;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class MyCalcApp {

	public static void main(String[] args) {
	 String filePath = "arabic_Poem.txt"; 
	
	        try (BufferedReader br = new BufferedReader(new InputStreamReader(
	                new FileInputStream(filePath), StandardCharsets.UTF_8))) {
	            String line;
	            while ((line = br.readLine()) != null) {
	                System.out.println(line);
	            }
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
}
}