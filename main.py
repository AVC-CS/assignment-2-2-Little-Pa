def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input('enter your temperature in Celsius: '))
        fahrenheit = 9 / 5 * celsius + 32
        
        print ('the converted temperature is ', fahrenheit)
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
