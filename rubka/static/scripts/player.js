const episodes_list = new Vue({
  delimiters: ["[[", "]]"],
  el: '#player',
  data() {
      return {
          seriesName: '',
          episodes: [],
          iframe: '',
      };
  },
  methods: {
      changeSeries(iframeCode) {
          this.iframe = iframeCode;
      },
  },
  async mounted() {
    const appElement = document.getElementById('player');
    this.seriesName = appElement.dataset.seriesName;

    if (!this.seriesName) {
        console.error("Ошибка: не найдено название сериала!");
        return;
    }

    try {
        const response = await fetch(`/api/series/all_episodes/${this.seriesName}/`);
        const data = await response.json();
        this.episodes = data;
        if (data.length > 0) {
            this.iframe = data[0].iframe; // Выбираем первую серию по умолчанию
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
  }
});

