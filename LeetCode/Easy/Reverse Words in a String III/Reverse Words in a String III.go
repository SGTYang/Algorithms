import strings

func reverseWords(s string) string {
	words := strings.Split(s, " ")
    
	var sb []string
    
	for _, word := range words {
		cb := []byte(word)
        
		for i, j := 0, len(cb)-1; i < j; i, j = i+1, j-1 {
			cb[i], cb[j] = cb[j], cb[i]
		}
		sb = append(sb, string(cb))
	}
	
	return strings.Join(sb, " ")
}
