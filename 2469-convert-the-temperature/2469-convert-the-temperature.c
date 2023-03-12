/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize){
    *returnSize = 2;
    double* far = (double*)malloc(2*sizeof(double));
    far[0] = celsius + 273.15;
    far[1] = celsius * 1.80 + 32.00;

    return (far);
}