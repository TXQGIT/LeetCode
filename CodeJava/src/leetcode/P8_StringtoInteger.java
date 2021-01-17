package leetcode;

import java.util.HashMap;
import java.util.Map;

class MealyMachine {
    public int sign;
    public long ans;
    public String state;
    private Map<String, String[]> stateTable = new HashMap<>();

    public MealyMachine() {
        this.sign = 1;
        this.ans = 0;
        this.state = "start";
        //当前状态为start
        // 输入为' '时, 转移到start状态;
        // 输入为'+'或者'-'时, 转移到signed状态;
        // 输入为数字时, 转移到in_number状态;
        // 输入为其他字符时, 转移到end状态.
        this.stateTable.put("start", new String[]{"start", "signed", "in_number", "end"});
        this.stateTable.put("signed", new String[]{"end", "end", "in_number", "end"});
        this.stateTable.put("in_number", new String[]{"end", "end", "in_number", "end"});
        this.stateTable.put("end", new String[]{"end", "end", "end", "end"});
    }

    public void get(char c) {
        state = stateTable.get(state)[getCol(c)];
        if("in_number".equals(state)) {
            ans = ans*10+(c-'0');
            ans = sign == 1 ? Math.min(ans, (long) Integer.MAX_VALUE) : Math.min(ans, -(long) Integer.MIN_VALUE);
        }else if("signed".equals(state)) {
            sign = c=='+' ? 1: -1;
        }
    }

    public int getCol(char c) {
        if (c == ' ') {
            return 0;
        }
        if (c == '+' || c == '-') {
            return 1;
        }
        if (Character.isDigit(c)) {
            return 2;
        }
        return 3;
    }
}

public class P8_StringtoInteger {
    //方法1：用if-else判断不同的条件
    public int caseWhenSolution(String s) {
        int sign = 1;
        long res = 0;
        boolean numberFlag = false;
        boolean signFlag = false;
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c==' ' && !numberFlag && !signFlag) { // "  +  413"的结果是0
                continue;
            }else if(c=='-' && !numberFlag && !signFlag) {  //" +-43"的结果是0
                signFlag = true;
                sign = -1;
            }else if(c=='+' && !numberFlag && !signFlag) { //" +-43"的结果是0
                signFlag = true;
            }else if ('0'<= c && c<='9') {
                numberFlag = true;
                res = res*10+(c-'0');
            }else {
                break;
            }
            //当前结果如果已经超过INT的限制,直接返回
            if(res*sign>Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }else if(res*sign<Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }
        res = sign*res;
        return (int)res;
    }

    //方法2：有限状态机
    public int dfaSolution(String s) {
        MealyMachine mealyMachine = new MealyMachine();
        for(int i=0; i<s.length(); i++) {
            mealyMachine.get(s.charAt(i));
        }
        return (int)(mealyMachine.sign * mealyMachine.ans);
    }

    public int myAtoi(String s) {
        //方法1：用if-else判断不同的条件
//        return caseWhenSolution(s);
        //方法2：有限状态机
        return dfaSolution(s);
    }

    public static void main(String[] args) {
        P8_StringtoInteger solution = new P8_StringtoInteger();
//        String s = "+91283472332";
        String s = " -43 12 e3";
        System.out.println(solution.myAtoi(s));
    }
}
