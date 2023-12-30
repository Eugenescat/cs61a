(define (my-filter func lst) 
    (if (= (length lst) 0)
        nil
        (if (func (car lst))
            (cons (car lst) (my-filter func (cdr lst)))
            (my-filter func (cdr lst)))))

(define (interleave s1 s2) 
    (cond ((= (length s1) 0) s2) 
          ; Each clause in a cond expression should be a list 
          ; with the condition as the first element and 
          ; the expression to evaluate if the condition is true 
          ; as the second element.
          (else (cons (car s1) (interleave s2 (cdr s1))))))

(define (accumulate merger start n term)
    (if (= n 0)
        start
        (accumulate merger (merger start (term n)) (- n 1) term)))

(define (no-repeats lst) 
    ; nil is not callablt, dont use ()
    (cond ((null? lst) nil)
    (else (cons (car lst) 
                (no-repeats 
                            (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst)))))))
