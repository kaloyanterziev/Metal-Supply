<template>
  <div :style="large ? 'width: 400px' : 'width: 200px'">
    <DoughnutChart class="align-content-center" v-bind="doughnutChartProps" />
  </div>
</template>

<script>
import { computed, defineComponent, ref } from "vue";

// eslint-disable-next-line no-unused-vars
import { Chart, ChartData, ChartOptions, registerables } from "chart.js";
Chart.register(...registerables);
import { DoughnutChart, useDoughnutChart } from "vue-chart-3";

export default defineComponent({
  name: "App",
  components: { DoughnutChart },
  props: ['dataValues', 'dataLabels', 'large'],
  setup(props)
  {
    const dataValues = ref(props.dataValues);
    const dataLabels = ref(props.dataLabels);

    const testData = computed(() => ({
      labels: dataLabels.value,
      datasets: [
        {
          data: dataValues.value,
          backgroundColor: [
            "#77CEFF",
            "#0079AF",
            "#123E6B",
            "#97B0C4",
            "#A5C8ED",
              "#77dd77",
              "#836953",
              "#89cff0",
              "#99c5c4"
          ],
        },
      ],
    }));

    const options = computed(() => ({
      scales: {
        myScale: {
          type: "logarithmic",
          position: "left",
        },
      },
      plugins: {
        legend: {
          position: "top"
        },
        title: {
          display: false,
          text: "Chart.js Doughnut Chart",
        },
      },
    }));

    const { doughnutChartProps, doughnutChartRef } = useDoughnutChart({
      chartData: testData,
      options,
    });

    return {
      testData,
      options,
      doughnutChartRef,
      doughnutChartProps,
    };
  }
});
</script>

<style scoped>

</style>
