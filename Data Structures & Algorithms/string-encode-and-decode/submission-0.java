class Solution {

    public String encode(List<String> strs) {
        StringBuilder result = new StringBuilder("");
        for (String str: strs) {
            result.append(str.length()).append("#").append(str);
        }
        return result.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < str.length()) {
            String sLength = "";
            while (str.charAt(index) != '#') {
                sLength = sLength + str.charAt(index);
                index++;
            }
            index++;
            int length = Integer.parseInt(sLength);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < length; i++) {
                sb.append(str.charAt(index));
                index++;
            }
            result.add(sb.toString());
        }
        return result;
    }
}








