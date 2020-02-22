class favourites:

    def numberOfBlocksAbove(self,array, block):
        
        elementsAbove = []
        # 1. remove all lines but those above 

        for element in array:
            if (element[1] > block[1]):
                elementsAbove.append(element)

        # 2. loop thrue remaining elements and count 
        LMR = [0, 0, 0]

        for element in elementsAbove:
            if(element[0] == 0):
                LMR[0] += 1

            if(element[0] == 1):
                LMR[1] += 1

            if(element[0] == 1):
                LMR[2] += 1
            
        # 3. return [L, M, R]
        print(' -------------------------- ')
        print('numberOfBlocksAbove: ')
        print(LMR)
        return LMR

    def massPointDisplacementFromMid (self, array, block):

        # tells how is mass arranged from middle block or center of row

        LMR = self.numberOfBlocksAbove(self, array, block)

        # Get number of blocks left and right columns.
        # Get different number ob blocks in columns, divided by total number of blocks in side columns.

        displacement = (LMR[2]-LMR[0])/(LMR[0]+LMR[2])
        print(' -------------------------- ')
        print('massPointDisplacementFromMid: ')
        print(displacement)
        return displacement


    def massPointDisplacementFromBlock (self, array, block):

         # tells how is mass arranged from  block itself,
        #  !!! implementation is kind of lacking !!! 

        LMR = self.numberOfBlocksAbove(self, array, block)
        # factor is based on different effect of distance from column
        factor = 1

        if( block[0] == 0):
            displacement = (LMR[1]*factor + LMR[2]) / (LMR[0]+ LMR[1]*factor + LMR[2])         

        if( block[0] == 1):
            displacement = self.massPointDisplacementFromMid(self, array, block)
        
        if( block[0] == 2):
             displacement = -(LMR[1]*factor + LMR[0]) / (LMR[0]+ LMR[1]*factor + LMR[2])

        print(' -------------------------- ')
        print('massPointDisplacementFromBlock: ')
        print(displacement)
        return displacement


