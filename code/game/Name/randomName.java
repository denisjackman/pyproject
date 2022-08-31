////////////////////////////
// Random Name Generator  //
// By Joshua Smyth        //
//                        //
// January 25, 2008       //
////////////////////////////

import java.util.*;

// Feel free to use/adapt/learn from this code or use it in your own projects or whatever :)

public class randomName
{
	//////////////////////////////
	/* Main Program Entry Point */
	//////////////////////////////
	public static void main(String args[])
	{
	// Get 12 random names
		for (int i=0;i<12;i++)
		{
			System.out.println(getRandomName());
		}
	}

	public static String getRandomName()
	{
		String retName = "";	// return this string

		// Seed random generator
		Random generator = new Random();

		int length = getRandomBetween(5,6);

		// CVCCVC or VCCVCV
		if(getRandomBetween(1,2) < 2)
		{
			retName += getRandomConsonant();
			retName = retName.toUpperCase();
			retName += getRandomVowel();
			retName += getRandomConsonant();
			retName += getRandomConsonant();
			if (length >= 5) { retName += getRandomVowel(); }
			if (length >= 6) { retName += getRandomConsonant(); }
		}
		else
		{
			retName += getRandomVowel();
			retName = retName.toUpperCase();
			retName += getRandomConsonant();
			retName += getRandomConsonant();
			retName += getRandomVowel();
			if (length >= 5) { retName += getRandomConsonant(); }
			if (length >= 6) { retName += getRandomVowel(); }
		}

		return retName;
	}

	// Returns a, e, i, o or u
	public static String getRandomVowel()
	{
		int randNum = getRandomBetween(1,4);

		switch(randNum)
		{
			case 1:
				return "a";
			case 2:
				return "e";
			case 3:
				return "i";
			case 4:
				return "o";
		}

		return "u";
	}

	public static String getRandomConsonant()
	{
		// Use the ascii values for a-z and convert to char
		char randLetter = (char) getRandomBetween(97,122);
		while (isCharVowel(randLetter))
		{
			randLetter = (char) getRandomBetween(97,122);
		}

		return Character.toString(randLetter);
	}

	public static boolean isCharVowel(char letter)
	{
		if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u')
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	// Returns a random number between lowerbound and upperbound inclusive
	public static int getRandomBetween(int lb, int ub)
	{
		Random generator = new Random();
		int ret = generator.nextInt(ub+1-lb) + lb;

		return ret;
	}
}