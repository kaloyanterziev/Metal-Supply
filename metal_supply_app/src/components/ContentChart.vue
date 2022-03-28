<template>
  <div style="width: 400px">
    <DoughnutChart v-bind="doughnutChartProps" />
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
  props: ['dataValues', 'dataLabels'],
  setup(props)
  {
    console.log(props.dataLabels, props.dataValues)
    const dataValues = ref(props.dataValues);
    const dataLabels = ref(props.dataLabels);
    // const dataValues = ref([30, 40, 60, 70, 5]);
    // const dataLabels = ref(["Paris", "Nîmes", "Toulon", "Perpignan", "Autre"]);

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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
