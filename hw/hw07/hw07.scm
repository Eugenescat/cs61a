(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s) 
    (if (<= (length s) 1)
        #t
        (if (> (car s) (cadr s))
            #f
            (ordered? (cdr s)))))

(define (square x) (* x x))

(define (pow base exp) 
    (if (= exp 0)
        1
        (if (= (modulo exp 2) 1)
            (* base (pow base (- exp 1)))
            (pow (square base) (/ exp 2)))))
