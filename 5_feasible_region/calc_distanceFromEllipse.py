import numpy as np
import math
import json

def calcdist(e_x, e_y, semi_major, semi_minor, angle, p):
  #Written by janblumenkamp at https://github.com/0xfaded/ellipse_demo/issues/1
  #Tanay Topac added (i)clamping and (ii)returning zero if the point is inside the ellipse
  def rot2d(angle):
      s, c = np.sin(angle), np.cos(angle)
      return np.array([[c,-s], [s, c]])

  p, p_ellipse = np.array(p), np.array([e_x, e_y])
  p_rot = rot2d(-angle).dot(p - p_ellipse)
  p_abs = np.abs(p_rot)
  t = np.array([0.707, 0.707])
  s = np.array([semi_major, semi_minor])
  ss_sub = (s*s)[0] - (s*s)[1]
  efac = np.array([ss_sub, -ss_sub])

  #Original (no clamp)
  # for _ in range(3):
  #     xy = s * t
  #     e = efac * (t ** 3) / s
  #     q = p_abs - e
  #     rq = np.linalg.norm(xy - e, 2) / np.linalg.norm(q, 2)
  #     t = (q * rq + e) / s
  #     t /= np.linalg.norm(t, 2)
  # p_edge = np.copysign(xy, p_rot)
  # dst = np.linalg.norm(p_edge - p_rot, 2)
  # p_edge_rot = rot2d(angle).dot(p_edge) + p_ellipse

  #Modified (w/clamp)
  for _ in range(3):
      xy = s * t
      e = efac * (t ** 3) / s
      q = p_abs - e
      rq = np.linalg.norm(xy - e, 2) / np.linalg.norm(q, 2)
      told = (q * rq + e) / s
      t0 = min(1.0, max(0.0, (q[0] * rq + e[0]) / s[0]))
      t1 = min(1.0, max(0.0, (q[1] * rq + e[1]) / s[1]))
      t = np.array([t0, t1])
      told /= np.linalg.norm(told, 2)
      t /= np.linalg.norm(t, 2)
      
  p_edgeold = np.copysign(xy, p_rot)
  p_edge = np.copysign(s*t, p_rot)
  dst = np.linalg.norm(p_edge - p_rot, 2)
  p_edge_rot = rot2d(angle).dot(p_edge) + p_ellipse

  #Add (returning zero if inside the ellipse)
  dst_nearestAbs_from_elpsctr = math.sqrt((e_x-p_edge_rot[0])**2 + (e_y-p_edge_rot[1])**2)
  dst_pAbs_from_elpsctr = math.sqrt((e_x-p[0])**2 + (e_y-p[1])**2)
  final_dst = dst if dst_pAbs_from_elpsctr > dst_nearestAbs_from_elpsctr else 0
  return final_dst, p_edge_rot #(Distance of point from nearest point on ellipse, nearest point on ellipse

if __name__ == "__main__":
  with open('ellipse_sml_def.json', 'r', encoding='utf-8') as f:
    ellipse = json.load(f)
  point = np.array([1,1])
  a = ellipse["a"]
  b = ellipse["b"]
  x0 = ellipse["x0"]
  y0 = ellipse["y0"]
  theta = ellipse["theta"]

  pointdist = calcdist(x0, y0, a, b, theta, point)
  print (pointdist)