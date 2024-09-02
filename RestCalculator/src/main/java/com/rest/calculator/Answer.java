package com.rest.calculator;

public class Answer {
	private double answer;
	  private double calculation;

	  public Answer(double answer, double calculation) {
	    this.answer = answer;
	    this.calculation = calculation;
	  }

	  public double getAnswer() {
	    return answer;
	  }

	  public double getCalculation() {
	    return calculation;
	  }
}
