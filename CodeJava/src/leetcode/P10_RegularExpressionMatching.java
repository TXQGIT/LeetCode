package leetcode;

public class P10_RegularExpressionMatching {

    public boolean dfsMatch(int ps, int pp, String s, String p) {
        if (pp<0) {
            return ps<0;
        }
        if (ps<0) {
            //如果pp<0说明都已经匹配了
            //如果pp>0,只有p中pp位置元素为*且满足*号前元素出现0次才行
            return pp<0 || (p.charAt(pp)=='*' && dfsMatch(ps, pp-2, s, p));
        }
        if (p.charAt(pp)=='.' || p.charAt(pp)==s.charAt(ps)) {
            return dfsMatch(ps-1, pp-1, s, p);
        }else if (p.charAt(pp)=='*') {
            //p中*前面的字符出现0次时的匹配结果
            boolean occurZero = dfsMatch(ps, pp-2, s, p);
            //p中*前面的字符出现至少1次时的匹配结果
            //*号前字符如果不为.或者和s.charAt(ps)不匹配的话, p中*前面的字符出现至少1次时无法和s匹配
            boolean occurLeastOne = ((p.charAt(pp-1)=='.' || s.charAt(ps)==p.charAt(pp-1)) && dfsMatch(ps-1, pp, s, p));
            return occurZero || occurLeastOne;
        }else {
            return false;
        }
    }

    public boolean isMatch(String s, String p) {
        return dfsMatch(s.length()-1, p.length()-1, s, p);
    }

    public static void main(String[] args) {
        String s = "aab";
        String p = "c*a*b";
        P10_RegularExpressionMatching solution = new P10_RegularExpressionMatching();
        System.out.println(solution.isMatch(s, p));
    }

}
