package com.rest.calculator;
import org.springframework.boot.SpringApplication;
	import org.springframework.boot.autoconfigure.SpringBootApplication;
	import org.springframework.http.HttpStatus;
	import org.springframework.http.ResponseEntity;
	import org.springframework.stereotype.Service;
	import org.springframework.web.bind.annotation.GetMapping;
	import org.springframework.web.bind.annotation.RequestParam;
	import org.springframework.web.bind.annotation.ResponseBody;
	import org.springframework.web.bind.annotation.RestController;

	import java.util.concurrent.atomic.AtomicLong;

	import javax.script.ScriptException;

	
@SpringBootApplication
@RestController
@Service	
public class CalcApp {
	

	  public static void main(String[] args) {
	    SpringApplication.run(CalcApp.class, args);
	  }


	  @GetMapping("/add")
	  public double add(@RequestParam(value = "num1",defaultValue = "")double num1, @RequestParam(value = "num2", defaultValue = "")double num2) {
		return num1+num2;	  
	  }
	  
	  @GetMapping("/sub")
	  public double sub(@RequestParam(value = "num1",defaultValue = "")double num1, @RequestParam(value = "num2", defaultValue = "")double num2) {
		return num1-num2;	  
	  }
	  
	  
}

