public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> mydict = new Dictionary<string, List<string>>();

        foreach (string word in strs)
        {
            char[] sortedChars = word.ToCharArray();
            Array.Sort(sortedChars);
            string sortedWord = new string(sortedChars);

            if (!mydict.ContainsKey(sortedWord)) 
            {
                mydict[sortedWord] = new List<string>();
            }
            mydict[sortedWord].Add(word);          
        }
        return new List<IList<string>>(mydict.Values);
    }
}