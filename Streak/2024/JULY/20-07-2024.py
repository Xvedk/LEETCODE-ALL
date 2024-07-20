from typing import *


class Solution:
    def restoreMatrix(
        self,
        rowSum: List[ int ],
        colSum: List[ int ]
        ) -> List[ List[ int ] ]:
        
        current_row = 0
        current_column = 0
        
        result = [
            [0] * len( colSum )
            for _ in range( len( rowSum) )
            ]
        
        while current_row <= len( rowSum ) - 1 and current_column <= len( colSum ) - 1:
            
            value_to_add = min(
                rowSum[ current_row ],
                colSum[ current_column ]
                )
            
            result[ current_row ][ current_column ] += value_to_add
            
            rowSum[ current_row ] -= value_to_add
            if not rowSum[ current_row ]:
                current_row += 1
            
            colSum[ current_column ] -= value_to_add
            if not colSum[ current_column ]:
                current_column += 1
        
        return result
    
    def check_result(
        self,
        matrix,
        rowSum,
        colSum
        ):
        
        return(
            all(
                [
                    sum( matrix[ row ] ) ==
                    rowSum[ row ]
                    for row in range( len( matrix ) )
                    ] +
                [
                    sum(
                        [
                            matrix[ row ][ column ]
                            for row in range( len( matrix ) )
                            ]
                        ) ==
                    colSum[ column ]
                    for column in range( len( matrix[0] ) )
                    ]
                )
        )
