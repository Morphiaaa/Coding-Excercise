import java.util.*;

public class numberOfPalindrome{
	public int count(String s){
		int count = 0;
		for (int i =0; i < s.length(); i++){
			for (int j = i+1; j < s.length(); j++){
				String substring = s.substring(i, j);
				if (isPalindrome(substring)){
					count ++;
				}
			}
		}
	return count;
	}

	public boolean isPalindrome(String s){
		int left = 0, right = s.length()-1;
		while (left < right) {
			if (s.charAt(left) != s.charAt(right)){
				return false;
			}
			else{
				left++;
				right--;
			}


		}
		return true;
	}


}