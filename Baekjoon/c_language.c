// 백준 C언어로 다시 문제 풀기
// studing..

#include 	<stdio.h>
#include	<stdlib.h>

// 각 반의 총 합 점수 구하는 함수
double	score_check(double *arr)
{
	int	i = 0;
	double score = 0;

	while (arr[i]) // 배열을 돌면서 score변수에 더함
	{
		score += arr[i];
		i++;
	}
	return (score); // 반환
}

// 총합의 평균을 초과하는 점수만 count해서 100분율 내서 반환하는 함수
double	class_check(void)
{
	double	*class;
	double	exam_score, total_score, student = 0, cnt = 0;
	int	idx = 0;

	scanf("%lf", &student); // 몇 명인지 input으로 받음
	class = (double *)malloc(sizeof(double) * student);
	if (!class)
		return (0);

	while (idx < student) // 각 학생의 점수를 배열에 저장
	{
		scanf("%lf", &exam_score);
		class[idx] = exam_score;
		idx++;
	}
	total_score = score_check(class); // 총점을 구하는 함수
	total_score /= student; // 총점을 학생수로 나눔 (평균)
	idx = 0;
	while (idx < student) // 평균 초과되는 인원 체크
	{
		if (total_score < class[idx])
			cnt++;
		idx++;
	}
	student = 100 / student; // 100분율을 구하기 위해 100을 학생수로 나눔
	//cnt *= student;
	return (cnt *= student); // 100으로 나눈 값과 평균을 넘는 학생을 곱해서 반환
}

int main(void)
{
	double	*class;
	int	class_num = 0, idx = 0;

	scanf("%d", &class_num); // 몇 반까지 있는지 input으로 받음
	class = (double *)malloc(sizeof(double) * class_num);
	if (!class)
		return (0);

	while (idx < class_num) // input으로 받은 반까지 반복문을 돌며 100분율 반환값을 배열에 저장
	{
		class[idx] = class_check(); // class_check func
		idx++;
	}
	idx = 0;
	while (idx < class_num) // 저장된 값을 %를 붙혀서 소수점 셋째 자리까지 출력
	{
		printf("%.3f%%\n", class[idx]);
		idx++;
	}
}
