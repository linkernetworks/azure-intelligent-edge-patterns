import * as R from 'ramda';

import { VideoAnno } from '../store/shared/BaseShape';

export type EnhanceVideoAnno = VideoAnno & {
  order: number;
};

export const plusOrderVideoAnnos = (videoAnnos: VideoAnno[]) => {
  return videoAnnos
    .sort((a, b) => {
      if (a.id > b.id) {
        return 1;
      }
      return -1;
    })
    .map((anno, i) => ({ ...anno, order: i + 1 }));
};
