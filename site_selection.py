# ============================================================ #
# Site Selection Using Genetic Algorithm (GA)                   #
# مکان‌یابی بهینه با استفاده از الگوریتم ژنتیک                  #
# ============================================================ #

import random

import matplotlib.pyplot as plt
import numpy as np
from deap import algorithms, base, creator, tools

# ============================================================ #
# 1. DATA GENERATION / تولید داده‌های ساختگی                    #
# ============================================================ #

np.random.seed(42)
n_points = 100
points = np.random.rand(n_points, 2) * 100                      # Candidate points
population = np.random.randint(50, 500, n_points)               # Population in 1km radius
libraries = np.random.rand(5, 2) * 100
hospitals = np.random.rand(3, 2) * 100
fire_stations = np.random.rand(3, 2) * 100


# ============================================================ #
# 2. FITNESS FUNCTION / تابع شایستگی                          #
# ============================================================ #

def fitness_function(selected_indices):
    """
    Calculate fitness for 3 selected points.
    محاسبه شایستگی برای ۳ نقطه‌ی انتخاب‌شده.
    """
    selected_points = points[selected_indices]

    # Criterion 1: Population coverage / پوشش جمعیت
    coverage = np.sum(population[selected_indices])

    # Criterion 2: Distance to facilities / فاصله از تسهیلات
    min_dist_lib = np.min([np.min(np.linalg.norm(p - libraries, axis=1)) for p in selected_points])
    min_dist_hosp = np.min([np.min(np.linalg.norm(p - hospitals, axis=1)) for p in selected_points])
    min_dist_fire = np.min([np.min(np.linalg.norm(p - fire_stations, axis=1)) for p in selected_points])

    # Criterion 3: Uniform spread / توزیع یکنواخت
    if len(selected_indices) == 3:
        d1 = np.linalg.norm(selected_points[0] - selected_points[1])
        d2 = np.linalg.norm(selected_points[1] - selected_points[2])
        d3 = np.linalg.norm(selected_points[2] - selected_points[0])
        spread = (d1 + d2 + d3) / 3
    else:
        spread = 0

    # Combine criteria (weighted sum) / ترکیب معیارها (مجموع وزنی)
    fitness = (coverage / 500) * 0.5 + (spread / 50) * 0.3 - (min_dist_lib + min_dist_hosp + min_dist_fire) * 0.2

    # ✅ CRITICAL: Return as a tuple of Python float
    # بازگشت به‌صورت یک تاپل از عدد اعشاری استاندارد پایتون
    return (float(fitness),)


# ============================================================ #
# 3. GENETIC ALGORITHM SETUP / تنظیمات الگوریتم ژنتیک         #
# ============================================================ #

# Create fitness and individual types / ایجاد انواع شایستگی و فرد
creator.create("FitnessMax", base.Fitness, weights=(1.0,))   # Maximization
creator.create("Individual", list, fitness=creator.FitnessMax)

# Register genetic operators / ثبت عملگرهای ژنتیکی
toolbox = base.Toolbox()

# Generate a random individual (3 unique indices)
toolbox.register("indices", random.sample, range(n_points), 3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation: explicitly return a tuple
toolbox.register("evaluate", lambda ind: (fitness_function(ind)[0],))

# Crossover, mutation, selection
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


# ============================================================ #
# 4. EXECUTION / اجرای الگوریتم                               #
# ============================================================ #

pop = toolbox.population(n=50)                      # Population size
hof = tools.HallOfFame(1)                           # Hall of Fame (best individual)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("max", np.max)

print("🔄 Running Genetic Algorithm...\n")

pop, log = algorithms.eaSimple(
    pop, toolbox,
    cxpb=0.5,       # Crossover probability
    mutpb=0.2,      # Mutation probability
    ngen=100,       # Number of generations
    stats=stats,
    halloffame=hof,
    verbose=True
)


# ============================================================ #
# 5. RESULTS / نتایج                                           #
# ============================================================ #

best = hof[0]  # Best solution

print("\n" + "="*60)
print("🏫 FINAL RESULT / نتیجه نهایی")
print("="*60)
print(f"📌 Selected indices / شاخص‌های انتخاب‌شده: {best}")
print(f"📍 Coordinates / مختصات: {points[best]}")
print(f"⭐ Fitness value / مقدار شایستگی: {fitness_function(best)[0]:.4f}")
print("="*60)


# ============================================================ #
# 6. PLOTTING / رسم نمودار                                     #
# ============================================================ #

plt.figure(figsize=(14, 10), facecolor='white')

# Candidate points
plt.scatter(points[:, 0], points[:, 1], c='blue', alpha=0.4, s=40,
            label='Candidate Points / نقاط کاندید')

# Selected schools (red stars)
plt.scatter(points[best, 0], points[best, 1], c='red', s=350, marker='*',
            edgecolors='black', linewidth=2,
            label='Selected Schools / مدارس انتخاب‌شده')

# Libraries (green triangles)
plt.scatter(libraries[:, 0], libraries[:, 1], c='green', marker='^', s=180,
            label='Libraries / کتابخانه‌ها')

# Hospitals (orange squares)
plt.scatter(hospitals[:, 0], hospitals[:, 1], c='orange', marker='s', s=180,
            label='Hospitals / بیمارستان‌ها')

# Fire stations (purple diamonds)
plt.scatter(fire_stations[:, 0], fire_stations[:, 1], c='purple', marker='D', s=180,
            label='Fire Stations / آتش‌نشانی‌ها')

# Annotate selected points
for i, idx in enumerate(best):
    plt.annotate(f'School #{i+1}', (points[idx, 0] + 2, points[idx, 1] + 2),
                 fontsize=13, fontweight='bold', color='darkred',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

plt.title('📍 Optimal School Site Selection using Genetic Algorithm\n'
          'مکان‌یابی بهینه مدارس با الگوریتم ژنتیک',
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel('X Coordinate / مختصات X', fontsize=13)
plt.ylabel('Y Coordinate / مختصات Y', fontsize=13)
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()

# Save figure
plt.savefig('site_selection_result.png', dpi=300, bbox_inches='tight')
print("📊 Plot saved as 'site_selection_result.png'")

plt.show()


# ============================================================ #
# 7. DONE / پایان                                              #
# ============================================================ #
print("\n" + "="*60)
print("✅ PROJECT COMPLETED SUCCESSFULLY / پروژه با موفقیت انجام شد")
print("="*60)
