package com.rest.calc;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CalcController {

    @GetMapping("/add")
    public String add(@RequestParam double num1, @RequestParam double num2) {
        double result = num1 + num2;
        return "Result: " + result;
    }

    @GetMapping("/subtract")
    public String subtract(@RequestParam double num1, @RequestParam double num2) {
        double result = num1 - num2;
        return "Result: " + result;
    }

}